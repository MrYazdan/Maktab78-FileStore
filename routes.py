from core.router import Router, Route, CallBack

router = Router("File Store Router", Route(
    "Main Menu",
    "Main menu description ...",
    children=(
        Route("About us", callback=CallBack("public.utils", "about_us")),

    )
))
