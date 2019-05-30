package de.wordclock;

import java.time.LocalTime;

public class LocalTimeProvider implements TimeProvider {

	@Override
	public int getMinutes() {
		LocalTime localTime = LocalTime.now();
		return localTime.getMinute();
	}

}
