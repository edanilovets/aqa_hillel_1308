# @pytest.fixture(autouse=True)
# def setup(app_auth: App):
#     # Setup
#     for pet_data in pet_data_list:
#         try:
#             app_auth.pet.delete_pet(pet_data["id"])
#         except RuntimeError:
#             pass
#     yield
#     # Teardown
#     for pet_data in pet_data_list:
#         try:
#             app_auth.pet.delete_pet(pet_data["id"])
#         except RuntimeError:
#             pass