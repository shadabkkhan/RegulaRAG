from app.ingestion.text_cleaner import clean_text

def test_func():

    input_string = "    SHADAB   KHAN    iffat   RBI   CIRCULAR  HELLO."
    expected_output = "SHADAB KHAN iffat RBI CIRCULAR HELLO."
    actual_output = clean_text(input_string)

    assert actual_output == expected_output, f"Expected '{expected_output}' but got '{actual_output}'"


def test_text_cleaner():
    input_string = "RBI CIRCULAR\n\n\nBanks must maintain security controls."
    expected_output = "RBI CIRCULAR\n\nBanks must maintain security controls."

    actual_output = clean_text(input_string)

    assert actual_output == expected_output, f"Expected '{expected_output}', but got '{actual_output}'"


def test_clean_text_empty_input():
    input_string = ""
    expected_output = ""

    actual_result = clean_text(input_string)

    assert actual_result == expected_output, f"expected '{expected_output}', but got '{actual_result}'"