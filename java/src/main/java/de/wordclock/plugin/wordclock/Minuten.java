package de.wordclock.plugin.wordclock;

public enum Minuten {
	NULL(""), FUENF_NACH("Fuenf Nach"), ZEHN_NACH("Zehn Nach"), VIERTEL_NACH("Viertel Nach"),
	ZWANZIG_NACH("Zwanzig Nach"), FUENF_UND_ZWANZIG_NACH("Fuenf Vor Halb"), HALB("Halb"),
	FUENF_UND_ZWANZIG_VOR("Fuenf Nach Halb"), ZWANZIG_VOR("Zwanzig Vor"), VIERTEL_VOR("Viertel Vor"),
	ZEHN_VOR("Zehn Vor"), FUENF_VOR("Fuenf Vor");

	private final String minuteValue;

	Minuten(String minuteValue) {
		this.minuteValue = minuteValue;
	}

	public String minuteValue() {
		return minuteValue;
	}

	public static String convertMinute(int minute) {
		int wordClockMinute = minute / 5;
		return values()[wordClockMinute].minuteValue();
	}
}
