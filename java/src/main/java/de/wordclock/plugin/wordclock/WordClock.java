package de.wordclock.plugin.wordclock;

import java.util.StringJoiner;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import de.wordclock.provider.TimeProvider;

@Service
public class WordClock {

	private static final String PREFIX = "Es Ist";
	private static final String POSTFIX = "Uhr";

	@Autowired
	private TimeProvider timeProvider;

	public String getConvertedTime() {
		int minute = timeProvider.getMinutes();
		int hour = timeProvider.getHour() % 12 + (minute / 5 > 4 ? 1 : 0);
		return buildTime(minute, hour);
	}

	private String buildTime(int minute, int hour) {
		StringJoiner timeAsString = new StringJoiner(" ");
		timeAsString.add(PREFIX);
		if (minute > 0) {
			timeAsString.add(Minuten.convertMinute(minute));
		}
		timeAsString.add(Stunden.convertStunde(hour));
		if (minute == 0) {
			timeAsString.add(POSTFIX);
		}
		return timeAsString.toString();
	}

}
