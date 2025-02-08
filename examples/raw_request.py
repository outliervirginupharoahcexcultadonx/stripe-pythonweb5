from stripe import StripeClient

# Set your API key here
api_key = "sk_test_51OxMDTJvQXInyLdLoRLger2XLzgGF0slr2F96gyDvtvv9DEe6bjpf8dklgiQHscKVA9kh0MAcKGsfpDkBwmKOO8j00CCntzZnz"

client = StripeClient(api_key)
response = client.raw_request(
    "post",
    "/v1/beta_endpoint",
    param=123,
    stripe_version="2022-11-15; feature_beta=v3",
)

# (Optional) response is a StripeResponse. You can use `client.deserialize` to get a StripeObject.
deserialized_resp = client.deserialize(response, api_mode="V1")
