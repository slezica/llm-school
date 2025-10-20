---
topic: Code Quality
trigger: Read before writing any code. This is a fundamental guide.
version: 1.0.0
---

# Code Quality

Pay close attention. These are the core principles of writing quality code.

1. **Simplicity**: write parts with only one purpose you can explain in only one sentence.
2. **Readability**: use structure and spacing to make room, group related things, separate sections and highlight patterns.
3. **Self-evidence**: names should immediately reveal the nature of the thing.
4. **Clarity**: prefer obvious code over clever code, even if it's longer.
5. **Observability**: add logs, metrics and traces to quickly spot what, where and how things break.
6. **Focus**: work only on the task at hand, don't start adding or changing unrelated behavior.
7. **Testing**: add tests as you add behavior to ensure correctness and detect regressions.
8. **Uniqueness**: avoid conceptual and textual duplication so that things exist in only one place.


## Examples

### Simplicity

Bad:
```python
def process(user, action):
    if user and user.is_active and not user.is_banned and user.has_permission(action) and (user.subscription_tier == 'premium' or user.trial_active) and datetime.now() < user.expiry_date:
        return execute_action(action)
    return None
```

Good:
```python
def can_perform_action(user, action):
    """Check if user has authorization to perform action."""
    if not user or not user.is_active or user.is_banned:
        return False
    if not user.has_permission(action):
        return False
    if datetime.now() >= user.expiry_date:
        return False
    return user.subscription_tier == 'premium' or user.trial_active

def process(user, action):
    if can_perform_action(user, action):
        return execute_action(action)
    return None
```


### Readability

Bad:
```javascript
function processOrders(orders) {
    const results = []
    for (let i = 0; i < orders.length; i++) {
        const order = orders[i]
        const total = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0)
        const tax = total * 0.08
        const shipping = total > 50 ? 0 : 5.99
        const final = total + tax + shipping
        results.push({id: order.id, total: final})
    }
    return results
}
```

Good:
```javascript
function processOrders(orders) {
    const results = []

    for (let i = 0; i < orders.length; i++) {
        const order = orders[i]

        const subtotal = order.items.reduce((sum, item) =>
            sum + item.price * item.quantity, 0
        )

        const tax = subtotal * 0.08
        const shipping = subtotal > 50 ? 0 : 5.99
        const total = subtotal + tax + shipping

        results.push({ id: order.id, total })
    }

    return results
}
```


### Self-evidence

Bad:
```python
def calc(u, a):
    d = datetime.now() - u.created
    if d.days < 30 and u.t == 'p':
        return a * 0.8
    return a
```

Good:
```python
def calculate_discounted_amount(user, amount):
    """Apply new user discount if eligible."""
    days_since_signup = datetime.now() - user.created_at
    is_new_user = days_since_signup.days < 30
    is_premium = user.subscription_tier == 'premium'

    if is_new_user and is_premium:
        return amount * 0.8  # 20% new user discount

    return amount
```


### Clarity

Bad:
```javascript
// Clever: use bitwise XOR to swap without temp variable
function swap(arr, i, j) {
    arr[i] ^= arr[j]
    arr[j] ^= arr[i]
    arr[i] ^= arr[j]
}
```

Good:
```javascript
// Obvious: use standard swap with temporary variable
function swap(arr, i, j) {
    const temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
}
```


### Observability

Bad:
```python
def process_payment(order):
    try:
        result = payment_gateway.charge(order.total)
        order.status = 'paid'
        return result
    except Exception:
        order.status = 'failed'
        return None
```

Good:
```python
def process_payment(order):
    logger.info(f"Processing payment for order {order.id}, amount: {order.total}")

    try:
        result = payment_gateway.charge(order.total)
        order.status = 'paid'

        logger.info(f"Payment successful for order {order.id}, transaction: {result.id}")
        metrics.increment('payments.success')

        return result

    except PaymentError as e:
        order.status = 'failed'

        logger.error(f"Payment failed for order {order.id}: {e.message}",
                    extra={'order_id': order.id, 'error_code': e.code})
        metrics.increment('payments.failure', tags={'reason': e.code})

        return None
```


### Focus

Bad:
```python
## Task: Add method to calculate order total

def calculate_order_total(order):
    total = sum(item.price * item.quantity for item in order.items)
    return total

## Also added email notification while working on this
def send_order_confirmation(order):
    email.send(order.user.email, f"Order total: ${order.total}")

## Also updated the user's last_order_date
def update_user_activity(user):
    user.last_order_date = datetime.now()
```

Good:
```python
## Task: Add method to calculate order total

def calculate_order_total(order):
    """Calculate total cost of all items in order."""
    total = sum(item.price * item.quantity for item in order.items)
    return total

## Task completed
```


### Testing

Bad:
```python
## Just implemented this new feature

def apply_bulk_discount(items):
    """Apply discount: 10% for 5+ items, 15% for 10+ items."""
    count = len(items)
    total = sum(item.price for item in items)

    if count >= 10:
        return total * 0.85
    elif count >= 5:
        return total * 0.90

    return total

## No tests written, will test manually later
```

Good:
```python
## Just implemented this new feature

def apply_bulk_discount(items):
    """Apply discount: 10% for 5+ items, 15% for 10+ items."""
    count = len(items)
    total = sum(item.price for item in items)

    if count >= 10:
        return total * 0.85
    elif count >= 5:
        return total * 0.90

    return total


## Tests written alongside implementation

def test_apply_bulk_discount():
    # No discount for fewer than 5 items
    items = [Item(price=10) for _ in range(4)]
    assert apply_bulk_discount(items) == 40

    # 10% discount for 5-9 items
    items = [Item(price=10) for _ in range(5)]
    assert apply_bulk_discount(items) == 45

    # 15% discount for 10+ items
    items = [Item(price=10) for _ in range(10)]
    assert apply_bulk_discount(items) == 85
```


### Uniqueness

Bad:
```javascript
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)
}

function validateUserEmail(user) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(user.email)
}

function checkEmailFormat(address) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return pattern.test(address)
}
```

Good:
```javascript
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

function isValidEmail(email) {
    return EMAIL_PATTERN.test(email)
}

function validateUser(user) {
    return isValidEmail(user.email)
}

function checkEmailFormat(address) {
    return isValidEmail(address)
}
```
