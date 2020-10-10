package de.wordclock.device;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class LoggerDevice implements IDevice {
	private final static Logger LOGGER = LoggerFactory.getLogger(LoggerDevice.class);

	@Override
	public void setState(String convertedTime) {
		LOGGER.info(convertedTime);
	}

}
