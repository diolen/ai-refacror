FRAMEWORK_ENTITIES = {
    "Auth",
    "Session",
    "Cookie",
    "RequestHandler",
    "Paginator",
    "Security",
    "Request",
    "Response",
    "Flash",
    "Configure",
    "Form"
}

HELPER_ENTITIES = {
    "Html",
    "FormHelper",
    "Js",
    "Time",
    "Number",
    "Text"
}


# =========================
# PURE NORMALIZATION (ID STABLE)
# =========================
def normalize(name):

    if not isinstance(name, str):
        return None

    name = name.strip()

    if not name:
        return None

    # ONLY trim method artifacts
    if name.endswith("()"):
        name = name[:-2]

    return name


# =========================
# CANONICAL KEY (CRITICAL FIX)
# =========================
def canonical(name):

    name = normalize(name)

    if not name:
        return None

    # stable identity rule (NO CASE DAMAGE)
    return name[0].upper() + name[1:] if len(name) > 1 else name.upper()


# =========================
# CLASSIFICATION
# =========================
def is_framework(name):

    name = canonical(name)

    if not name:
        return False

    return name in FRAMEWORK_ENTITIES


def is_helper(name):

    name = canonical(name)

    if not name:
        return False

    return name in HELPER_ENTITIES


# =========================
# DOMAIN FILTER
# =========================
def is_valid_domain_entity(name):

    name = canonical(name)

    if not name:
        return False

    if is_framework(name):
        return False

    if is_helper(name):
        return False

    if name.lower() in {"domain", "framework", "helper"}:
        return False

    return True