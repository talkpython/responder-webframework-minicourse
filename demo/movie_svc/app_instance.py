import responder

# CORS wasn't demoed in the course, but is required to be used from
# external apps like movie exploder.

cors_params = {
    'allow_origins': '*',
    'allow_methods': '*',
}

api = responder.API(cors=True, cors_params=cors_params)
