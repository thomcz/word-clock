package de.wordclock.plugin.wordclock;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import de.wordclock.plugin.wordclock.WordClockMinuten;
import de.wordclock.provider.TimeProvider;

public class WordClockMinutenTest {
	private TimeProvider timeProvider;

	@BeforeEach
	public void setUp() {
		timeProvider = mock(TimeProvider.class);
	}

	@ParameterizedTest
	@ValueSource(ints = { 0, 1, 2, 3, 4 })
	public void zeroMinuteTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert)).isEqualTo(WordClockMinuten.NULL.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 5, 6, 7, 8, 9 })
	public void fuenfNachTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.FUENF_NACH.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 10, 11, 12, 13, 14 })
	public void zehnNachTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.ZEHN_NACH.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 15, 16, 17, 18, 19 })
	public void viertelNachTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.VIERTEL_NACH.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 20, 21, 22, 23, 24 })
	public void zwanzigNachTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.ZWANZIG_NACH.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 25, 26, 27, 28, 29 })
	public void fuenfUndZwanzigNachTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.FUENF_UND_ZWANZIG_NACH.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 30, 31, 32, 33, 34 })
	public void halbTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert)).isEqualTo(WordClockMinuten.HALB.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 35, 36, 37, 38, 39 })
	public void fuenfUndZwanzigVorTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.FUENF_UND_ZWANZIG_VOR.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 40, 41, 42, 43, 44 })
	public void zwanzigVorTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.ZWANZIG_VOR.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 45, 46, 47, 48, 49 })
	public void viertelVorTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.VIERTEL_VOR.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 50, 51, 52, 53, 54 })
	public void zehnVorTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert)).isEqualTo(WordClockMinuten.ZEHN_VOR.minuteValue());
	}

	@ParameterizedTest
	@ValueSource(ints = { 55, 56, 57, 58, 59 })
	public void fuenfVorTest(int minute) {
		when(timeProvider.getMinutes()).thenReturn(minute);
		int minutesToConvert = timeProvider.getMinutes();
		assertThat(WordClockMinuten.convertMinute(minutesToConvert))
				.isEqualTo(WordClockMinuten.FUENF_VOR.minuteValue());
	}

}
