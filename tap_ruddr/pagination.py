from singer_sdk.pagination import JSONPathPaginator, BaseAPIPaginator

class ruddrPaginator(BaseAPIPaginator):

    def get_next(self, response):
        body: dict = response.json()
        hasMore = body.get("hasMore")

        # if no more results, stop pagination
        if not hasMore:
            return

        # leverage JSONPathPaginator to lookup the id of the last result
        return JSONPathPaginator("$[-1:].id").get_next(response)