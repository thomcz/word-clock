package de.wordclock.plugin.wordclock;

import java.util.StringJoiner;
import java.util.concurrent.TimeUnit;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import de.wordclock.device.LoggerDevice;
import de.wordclock.provider.TimeProvider;

@Service
public class WordClock implements Plugin {

	private static final String PREFIX = "Es Ist";
	private static final String POSTFIX = "Uhr";

	@Autowired
	private TimeProvider timeProvider;

	@Autowired
	private LoggerDevice device;

	@Override
	public void run() {
		while (!Thread.interrupted()) {
			try {
				device.setState(getConvertedTime());
				TimeUnit.SECONDS.sleep(1);
			} catch (InterruptedException e) {
				Thread.currentThread().interrupt();
			}
		}
	}

	public String getConvertedTime() {
		int minute = timeProvider.getMinutes();
		int hour = timeProvider.getHour() % 12 + (minute / 5 > 4 ? 1 : 0);
		return buildTime(minute, hour);
	}

	private String buildTime(int minutes, int hour) {
		StringJoiner timeAsString = new StringJoiner(" ");
		timeAsString.add(PREFIX);
		if (minutes >= 5) {
			timeAsString.add(Minuten.convertMinute(minutes));
		}
		timeAsString.add(Stunden.convertStunde(hour));
		if (minutes < 5) {
			timeAsString.add(POSTFIX);
		}
		return timeAsString.toString();
	}

}
