"""Request handler for settlement-checksum."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "settlement-checksum"}
