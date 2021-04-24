from feed.feed_request import Feed

feed_obj = Feed(feed_type='item',
				feed_scope='ALL_ACTIVE',
				category_id='6000',
				marketplace_id='EBAY_US',
				token='none',
				environment='PRODUCTION')
feed_obj.get()