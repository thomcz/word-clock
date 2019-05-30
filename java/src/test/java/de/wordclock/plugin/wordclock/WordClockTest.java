package de.wordclock.plugin.wordclock;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.when;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.boot.test.context.SpringBootTest;

import de.wordclock.plugin.wordclock.WordClock;
import de.wordclock.plugin.wordclock.WordClockMinuten;
import de.wordclock.plugin.wordclock.WordClockStunden;
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
		String expected = String.format("%s %s %s", PREFIX, WordClockStunden.convertStunde(hour), POSTFIX);
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(5);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(5),
				WordClockStunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zehnNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(10);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(10),
				WordClockStunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void viertelNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(15);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(15),
				WordClockStunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zwanzigNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(20);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(20),
				WordClockStunden.convertStunde(hour));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfUndZwanzigNachTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(25);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(25),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void halbTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(30);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(30),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfUndZwanzigVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(35);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(35),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zwanzigVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(40);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(40),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void viertelVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(45);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(45),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void zehnVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(50);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(50),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 })
	public void fuenfVorTest(int hour) {
		when(timeProvider.getHour()).thenReturn(hour);
		when(timeProvider.getMinutes()).thenReturn(55);
		String expected = String.format("%s %s %s", PREFIX, WordClockMinuten.convertMinute(55),
				WordClockStunden.convertStunde(hour + 1));
		assertThat(wordClock.getConvertedTime()).isEqualTo(expected);
	}

}
