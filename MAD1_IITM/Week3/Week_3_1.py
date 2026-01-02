import pyhtml as h

t = h.html(
    h.head(
        h.title("Test")
    ),
    h.body(
        h.h1("Heading"),
        h.p("paragraph")
    )
)

print(t.render())