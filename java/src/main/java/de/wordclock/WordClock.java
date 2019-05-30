package de.wordclock;

public class WordClock {

	public String convertMinute(int minute) {
		int wordClockMinute = minute / 5;
		return WordClockMinuten.values()[wordClockMinute].minuteValue();
	}

}
