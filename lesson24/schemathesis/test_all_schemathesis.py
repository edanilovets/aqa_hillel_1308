# import schemathesis
# from schemathesis.checks import status_code_conformance
#
# schema = schemathesis.from_uri("https://petstore.swagger.io/v2/swagger.json")
#
# @schema.parametrize()
# def test_api(case):
#     case.call_and_validate(checks=(status_code_conformance,))