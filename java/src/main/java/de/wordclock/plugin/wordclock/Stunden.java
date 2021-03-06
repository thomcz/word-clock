package de.wordclock.plugin.wordclock;

public enum Stunden {
	NULL("Zwoelf"), EIN("Eins"), ZWEI("Zwei"), DREI("Drei"), VIER("Vier"), FUENF("Fuenf"), SECHS("Sechs"),
	SIEBEN("Sieben"), ACHT("Acht"), NEUN("Neun"), ZEHN("Zehn"), ELF("Elf"), ZWOELF("Zwoelf");

	private final String stundeValue;

	Stunden(String stundeValue) {
		this.stundeValue = stundeValue;
	}

	public String stundenValue() {
		return stundeValue;
	}

	public static String convertStunde(int stunde) {
		int wordClockHour = stunde % 12;
		return values()[wordClockHour].stundenValue();
	}
}
