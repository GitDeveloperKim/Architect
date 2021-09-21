package cleancode;

import static org.junit.Assert.*;

import org.junit.Test;

public class CalculatorTest {

	@Test
	public void testSum() {
		Calculator cal = new Calculator();
		assertEquals(30, cal.add(10,20));
	}

}
