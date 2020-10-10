package de.wordclock.plugin.wordclock;

import de.wordclock.device.IDevice;
import de.wordclock.provider.TimeProvider;
import org.springframework.stereotype.Service;

import java.util.StringJoiner;

@Service
public class WordClock implements Plugin {
 
    private static final String PLUGIN_NAME = "WORD_CLOCK";
    private static final String PREFIX = "Es Ist";
    private static final String POSTFIX = "Uhr";

    private final TimeProvider timeProvider;

    private final IDevice device;

    public WordClock(TimeProvider timeProvider, IDevice device) {
        this.timeProvider = timeProvider;
        this.device = device;
    }

    @Override
    public void run() {
        device.setState(getConvertedTime());
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

    @Override
    public String getPluginName() {
        return PLUGIN_NAME;
    }
}
