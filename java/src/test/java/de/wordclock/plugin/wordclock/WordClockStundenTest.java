package de.wordclock.plugin.wordclock;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import de.wordclock.plugin.wordclock.WordClockStunden;
import de.wordclock.provider.TimeProvider;

public class WordClockStundenTest {
	private TimeProvider timeProvider;

	@BeforeEach
	public void setUp() {
		timeProvider = mock(TimeProvider.class);
	}

	@Test
	public void midnightTest() {
		when(timeProvider.getHour()).thenReturn(0);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.NULL.stundenValue());
	}

	@Test
	public void anHourTest() {
		when(timeProvider.getHour()).thenReturn(1);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.EIN.stundenValue());
	}

	@Test
	public void twoOClockTest() {
		when(timeProvider.getHour()).thenReturn(2);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.ZWEI.stundenValue());
	}

	@Test
	public void threeOClockTest() {
		when(timeProvider.getHour()).thenReturn(3);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.DREI.stundenValue());
	}

	@Test
	public void fourOClockTest() {
		when(timeProvider.getHour()).thenReturn(4);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.VIER.stundenValue());
	}

	@Test
	public void fiveOClockTest() {
		when(timeProvider.getHour()).thenReturn(5);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.FUENF.stundenValue());
	}

	@Test
	public void sixOClockTest() {
		when(timeProvider.getHour()).thenReturn(6);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.SECHS.stundenValue());
	}

	@Test
	public void sevenOClockTest() {
		when(timeProvider.getHour()).thenReturn(7);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.SIEBEN.stundenValue());
	}

	@Test
	public void eightOClockTest() {
		when(timeProvider.getHour()).thenReturn(8);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.ACHT.stundenValue());
	}

	@Test
	public void nineOClockTest() {
		when(timeProvider.getHour()).thenReturn(9);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.NEUN.stundenValue());
	}

	@Test
	public void tenOClockTest() {
		when(timeProvider.getHour()).thenReturn(10);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.ZEHN.stundenValue());
	}

	@Test
	public void elevenOClockTest() {
		when(timeProvider.getHour()).thenReturn(11);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.ELF.stundenValue());
	}

	@Test
	public void twelveOClockTest() {
		when(timeProvider.getHour()).thenReturn(12);
		int hourToConvert = timeProvider.getHour();
		assertThat(WordClockStunden.convertStunde(hourToConvert)).isEqualTo(WordClockStunden.ZWOELF.stundenValue());
	}

}
