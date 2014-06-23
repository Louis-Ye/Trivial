#
# Author:
# 	Louis Ye
#
# Description:
# 	This script is only for subtitles file of .srt format
#
# How to use (for instance):
#	perl showingSubtitles.pl ./21-jump-street-yify-english.srt
#


use strict;
use warnings;

use Time::HiRes qw(usleep);
use Time::HiRes qw(time);

if ($#ARGV ne 0) {
	print "There should only be one parameters.\n";
	exit 1;
}

my $subtitlesFile = $ARGV[0];
my @startTimeP = ();
my @endTimeP = ();
my @subtitleSentence = ();
my $currentNum = -1;
my $lineNumber = 0;
my $isFirstLine = 1;

print "Loading subtitles file ...\n";
open FILE, "$subtitlesFile" or die $!;
for my $oriLine (<FILE>) {
	if ($isFirstLine) {
		$isFirstLine = 0;
		$oriLine = "0\r\n";
	}

	my $line = getNormalLine($oriLine);
	 print "$line\n";
	if ($line =~ /^(\d+):(\d+):(\d+),(\d+)\s--\>\s(\d+):(\d+):(\d+),(\d+)/) {
		my $startTime = ($1 * 60.0 * 60.0 + $2 * 60.0 + $3) + $4 / 1000.0;
		my $endTime = ($5 * 60.0 * 60.0 + $6 * 60.0 + $7) + $8 / 1000.0;
		push(@startTimeP, $startTime);
		push(@endTimeP, $endTime);
		push(@subtitleSentence, "");
		$currentNum += 1;
	}
	elsif ( $line =~ /^(\d+)/ ) {
	}
	else {
		$subtitleSentence[$currentNum] .= "$line\n";
	}

	$lineNumber += 1;
	# if ($lineNumber > 20) {
	# 	last;
	# }
}
close FILE;


my $length = @subtitleSentence;
print "The srt subtitles file is ready now, $length subtitles in total\n";
print "press ENTER to start playing\n";
my $input = <STDIN>;

print "3...\n";
sleep 1;
print "2...\n";
sleep 1;
print "1...\n";
sleep 1;
print "go! \n";
sleep 1;

my $i = 0;
my $startingTime = time;

while (1) {
	my $currentTime = time;

	if ($currentTime > $startingTime + $startTimeP[$i]) {
		system("clear");
		print $subtitleSentence[$i];
		$i += 1;
		sleep 0;
	}
	if ($i >= $length - 1) {
		last;
	}

	usleep(1000);
}



exit 0;






sub getNormalLine {
	my $oriLine = shift;
	my $normalLine = "";
	my @sp = split //, $oriLine;
	for my $c (@sp) {
		if (($c eq "\n") or ($c eq "\r")) {
		}
		elsif ($c =~ /[\,\w\d\:\-\>\<\ \']/) {
			$normalLine .= $c;
		}
	}
	return $normalLine;
}

