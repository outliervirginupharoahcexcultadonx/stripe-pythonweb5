# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._coupon import Coupon
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CouponService(StripeService):
    class CreateParams(TypedDict):
        amount_off: NotRequired[int]
        """
        A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed).
        """
        applies_to: NotRequired["CouponService.CreateParamsAppliesTo"]
        """
        A hash containing directions for what this Coupon will apply discounts to.
        """
        currency: NotRequired[str]
        """
        Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).
        """
        currency_options: NotRequired[
            Dict[str, "CouponService.CreateParamsCurrencyOptions"]
        ]
        """
        Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """
        duration: NotRequired[Literal["forever", "once", "repeating"]]
        """
        Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`.
        """
        duration_in_months: NotRequired[int]
        """
        Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        id: NotRequired[str]
        """
        Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you.
        """
        max_redemptions: NotRequired[int]
        """
        A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired[str]
        """
        Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
        """
        percent_off: NotRequired[float]
        """
        A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).
        """
        redeem_by: NotRequired[int]
        """
        Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers.
        """

    class CreateParamsAppliesTo(TypedDict):
        products: NotRequired[List[str]]
        """
        An array of Product IDs that this Coupon will apply to.
        """

    class CreateParamsCurrencyOptions(TypedDict):
        amount_off: int
        """
        A positive integer representing the amount to subtract from an invoice total.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        created: NotRequired["CouponService.ListParamsCreated|int"]
        """
        A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired[int]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired[int]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired[int]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired[int]
        """
        Maximum value to filter by (inclusive)
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        currency_options: NotRequired[
            Dict[str, "CouponService.UpdateParamsCurrencyOptions"]
        ]
        """
        Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired[str]
        """
        Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
        """

    class UpdateParamsCurrencyOptions(TypedDict):
        amount_off: int
        """
        A positive integer representing the amount to subtract from an invoice total.
        """

    def delete(
        self,
        coupon: str,
        params: "CouponService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Coupon:
        """
        You can delete coupons via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can't redeem the coupon. You can also delete coupons via the API.
        """
        return cast(
            Coupon,
            self._request(
                "delete",
                "/v1/coupons/{coupon}".format(coupon=sanitize_id(coupon)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        coupon: str,
        params: "CouponService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Coupon:
        """
        Retrieves the coupon with the given ID.
        """
        return cast(
            Coupon,
            self._request(
                "get",
                "/v1/coupons/{coupon}".format(coupon=sanitize_id(coupon)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        coupon: str,
        params: "CouponService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Coupon:
        """
        Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.
        """
        return cast(
            Coupon,
            self._request(
                "post",
                "/v1/coupons/{coupon}".format(coupon=sanitize_id(coupon)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "CouponService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Coupon]:
        """
        Returns a list of your coupons.
        """
        return cast(
            ListObject[Coupon],
            self._request(
                "get",
                "/v1/coupons",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CouponService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Coupon:
        """
        You can create coupons easily via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

        A coupon has either a percent_off or an amount_off and currency. If you set an amount_off, that amount will be subtracted from any invoice's subtotal. For example, an invoice with a subtotal of 100 will have a final total of 0 if a coupon with an amount_off of 200 is applied to it and an invoice with a subtotal of 300 will have a final total of 100 if a coupon with an amount_off of 200 is applied to it.
        """
        return cast(
            Coupon,
            self._request(
                "post",
                "/v1/coupons",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
