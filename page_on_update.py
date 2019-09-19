import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import argparse
import json
import urllib2
import time

parser = argparse.ArgumentParser(
    description='Grab page content periodically and send notificaton when the page is updated')
parser.add_argument('-i', '--input_file', metavar='input json file', type=str, required=True,
                    help='The file contains the input and configuration information in json format.')
args = parser.parse_args()

def SendEmail(input_json):
    msg = MIMEMultipart()
    msg['From'] = input_json['SOURCE_EMAIL']
    msg['To'] = input_json['TARGET_EMAIL']
    msg['Subject'] = input_json['EMAIL_TITLE']
    msg.attach(MIMEText(input_json['EMAIL_CONTENT']))

    smtp_server = smtplib.SMTP(input_json['SMTP_SERVER'], int(input_json['SMTP_PORT']))
    # Ientify myself to the SMTP server
    smtp_server.ehlo()
    # Secure TLS encryption
    smtp_server.starttls()
    # Re-identify as an encrypted connection
    smtp_server.ehlo()
    smtp_server.login(input_json['SOURCE_EMAIL'], input_json['SOURCE_PASSWORD'])
    smtp_server.sendmail(input_json['SOURCE_EMAIL'], input_json['TARGET_EMAIL'], msg.as_string())
    smtp_server.quit()


def main(): 
    with open(args.input_file) as f:
        input_json = json.load(f)
        while True:
            response = urllib2.urlopen(input_json['PAGE_URL'])
            html = str(response.read())
            for item in input_json['TRIGGER_ITEMS_DISAPPEAR']:
                if html.find(str(item)) == -1:
                    SendEmail(input_json)
                    return
            time.sleep(input_json['REFRESH_PERIOD_SEC'])

if __name__ == "__main__":
    main()