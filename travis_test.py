from obscurecove import read_string_from_file

############################################################

def test_obscurecove():

    print("testing obscurecove")

    assert read_string_from_file(None, "default") == "default"

############################################################
