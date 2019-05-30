package de.wordclock.plugin.wordclock;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import de.wordclock.plugin.wordclock.Stunden;
import de.wordclock.provider.TimeProvider;

public class StundenTest {
	private TimeProvider timeProvider;

	@BeforeEach
	public void setUp() {
		timeProvider = mock(TimeProvider.class);
	}

	@Test
	public void midnightTest() {
		when(timeProvider.getHour()).thenReturn(0);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.NULL.stundenValue());
	}

	@Test
	public void anHourTest() {
		when(timeProvider.getHour()).thenReturn(1);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.EIN.stundenValue());
	}

	@Test
	public void twoOClockTest() {
		when(timeProvider.getHour()).thenReturn(2);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.ZWEI.stundenValue());
	}

	@Test
	public void threeOClockTest() {
		when(timeProvider.getHour()).thenReturn(3);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.DREI.stundenValue());
	}

	@Test
	public void fourOClockTest() {
		when(timeProvider.getHour()).thenReturn(4);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.VIER.stundenValue());
	}

	@Test
	public void fiveOClockTest() {
		when(timeProvider.getHour()).thenReturn(5);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.FUENF.stundenValue());
	}

	@Test
	public void sixOClockTest() {
		when(timeProvider.getHour()).thenReturn(6);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.SECHS.stundenValue());
	}

	@Test
	public void sevenOClockTest() {
		when(timeProvider.getHour()).thenReturn(7);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.SIEBEN.stundenValue());
	}

	@Test
	public void eightOClockTest() {
		when(timeProvider.getHour()).thenReturn(8);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.ACHT.stundenValue());
	}

	@Test
	public void nineOClockTest() {
		when(timeProvider.getHour()).thenReturn(9);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.NEUN.stundenValue());
	}

	@Test
	public void tenOClockTest() {
		when(timeProvider.getHour()).thenReturn(10);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.ZEHN.stundenValue());
	}

	@Test
	public void elevenOClockTest() {
		when(timeProvider.getHour()).thenReturn(11);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.ELF.stundenValue());
	}

	@Test
	public void twelveOClockTest() {
		when(timeProvider.getHour()).thenReturn(12);
		int hourToConvert = timeProvider.getHour();
		assertThat(Stunden.convertStunde(hourToConvert)).isEqualTo(Stunden.ZWOELF.stundenValue());
	}

}
