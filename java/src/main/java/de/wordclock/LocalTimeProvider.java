package de.wordclock;

import java.time.LocalTime;

import org.springframework.stereotype.Service;

@Service
public class LocalTimeProvider implements TimeProvider {

	@Override
	public int getMinutes() {
		return LocalTime.now().getMinute();
	}

	@Override
	public int getHour() {
		return LocalTime.now().getHour();
	}

}
