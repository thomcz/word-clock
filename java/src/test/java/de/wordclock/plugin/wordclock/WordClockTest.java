package de.wordclock.plugin.wordclock;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.when;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.boot.test.context.SpringBootTest;

import de.wordclock.provider.TimeProvider;

@SpringBootTest
public class WordClockTest {
	private static final String PREFIX = "Es Ist";
	private static final String POSTFIX = "Uhr";
	@InjectMocks
	private WordClock wordClock;
	@Mock
	private TimeProvider timeProvider;

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fullHourTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		String expected = String.format("%s %s %s", PREFIX, Stunden.convertStunde(hour), POSTFIX);
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4 })
	public void fullHourLessThanFiveMinutesTest(int minutes) {
		when(timeProvider.getHour()).thenReturn(1);
		when(timeProvider.getMinutes()).thenReturn(minutes);
		String expected = String.format("%s %s %s", PREFIX, Stunden.convertStunde(1), POSTFIX);
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(5);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(5), Stunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zehnNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(10);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(10), Stunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void viertelNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(15);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(15), Stunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zwanzigNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(20);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(20), Stunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfUndZwanzigNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(25);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(25), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void halbTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(30);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(30), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfUndZwanzigVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(35);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(35), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zwanzigVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(40);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(40), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void viertelVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(45);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(45), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zehnVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(50);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(50), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(55);
		String expected = String.format("%s %s %s", PREFIX, Minuten.convertMinute(55), Stunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

}
