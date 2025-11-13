---
topic: Writing Code
trigger: Read before designing architecture, specifying behavior, setting up new projects or writing code yourself (i.e. when not delegating to an agent). This is a fundamental guide.
version: 1.0.0
---

# Writing Code

Pay close attention. These are the core principles of writing quality code.

1. **Simplicity**: write parts with only one purpose you can explain in only one sentence.
2. **Readability**: use structure and spacing to make room, group related things, separate sections and highlight patterns.
3. **Self-evidence**: names should immediately reveal the nature of the thing.
4. **Clarity**: prefer obvious code over clever code, even if it's longer.
5. **Observability**: add logs, metrics and traces to quickly spot what, where and how things break.
6. **Testing**: add tests as you add behavior to ensure correctness and detect regressions, without overtesting.
7. **Annotation**: add strategic comments and docstrings to complement code without cluttering or being redundant.
8. **Versioning**: use `git` to commit implementation steps to individual parts with concise comments.


## Examples

### Simplicity

Bad:
```javascript
function processOrders(orders) {
    const results = []

    for (let i = 0; i < orders.length; i++) {
        // Calculate a bunch of stuff with magic numbers and complex logic:
        const order = orders[i]
        const total = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0)
        const tax = total * 0.08
        const shipping = total > 50 ? 0 : 5.99
        const final = total + tax + shipping
        results.push({id: order.id, total: final})

        // Also emit notifications:
        notificationService.notify(order)

        // Also save to the database:
        order.setHandled(true)
        order.save()
    }

    return results
}
```

Good:
```javascript
function processOrders(orders, context) {
    const results = []

    for (let order of orders) {
        const totals = calculateTotals(order, context)
        results.push({ order, totals })

        notifyBuyers(order, context)
    }

    return results
}

function calculateTotals(order, context) {
    let subtotal = 0
    for (let item of order.items) {
        subtotal += item.price * item.quantity
    }

    const tax = subtotal * context.taxRate
    const shipping = (subtotal > context.minFreeShippingPrice) ? 0 : context.baseShippingPrice
    const total = subtotal + tax + shipping

    return { subtotal, tax, shipping, total }
}

function notifyBuyers(order, context) {
    context.notificationService.notify(order)
}
```


### Readability

Bad:
```python
def process(user, action):
    if user and user.is_active and not user.is_banned and user.has_permission(action) and (user.subscription_tier == 'premium' or user.trial_active) and datetime.now() < user.expiry_date:
        action.execute()
```

Good:
```python
def can_execute_action(user, action):
    if not user or not user.is_active or user.is_banned:
        return False

    if not user.has_permission(action):
        return False

    if datetime.now() >= user.expiry_date:
        return False

    else:
        return user.subscription_tier == 'premium' or user.trial_active

def process(user, action):
    if can_execute_action(user, action):
        action.execute()

    return None
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
return groups.reduce((arr, max) => arr.map(u => calculateAge(u)).some(a => a > max))
```

Good:
```javascript
for (let group of groups) {
    for (let member of group) {
        if (calculateAge(member) > max) {
            return true
        }
    }
}

return false
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

        logger.error( f"Payment failed for order {order.id}: {e.message}", extra={
            'order_id': order.id,
            'reason': e.code,
        })

        metrics.increment('payments.failure', tags={'reason': e.code})

        raise e # let caller decide
```


### Testing

Bad:
```python
## Just implemented this new feature

def apply_bulk_discount(items):
    count = len(items)
    total = sum(item.price for item in items)

    if count >= 10:
        return total * 0.85
    elif count >= 5:
        return total * 0.90
    else:
        return total

## No tests written, will test manually later
```

Good:
```python
## Just implemented this new feature

def apply_bulk_discount(items):
    count = len(items)
    total = sum(item.price for item in items)

    if count >= 10:
        return total * 0.85
    elif count >= 5:
        return total * 0.90
    else:
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

Bad (test is excessive, extremely basic behavior of code):
```python
def test_object_can_be_constructed_with_its_properties():
    o = SomeObj(12, "haha", 2.5)
    assert o.number == 12
    assert o.name == "haha"
    assert o.fraction == 2.5
```


### Annotation

Bad:
```python
def calculate_difference(x, y):
    """Calculate the difference between x and y"
    d = x - y # subtract y

    # NOTE:
    # Calculation involves subtraction

    return d
```

Good:
```python
def calculate_difference(x, y):
    return = x - y # this will always be positive, since we know y < x
```

Bad:
```python
def calculate_effective_value(self, attribute_name: str) -> float:
    """Calculate the effective value of an attribute with bonuses.

    Args:
        attribute_name: Name of the attribute to calculate

    Returns:
        Final attribute value after applying all bonuses

    Raises:
        KeyError: If the attribute doesn't exist on this character
    """

    if attribute_name not in self.attributes:
        raise KeyError(f"Character '{self.name}' does not have attribute '{attribute_name}'")

    # ... continues
```

Good:
```python
def calculate_effective_value(self, attribute_name: str) -> float:
    attribute = self.attributes[attribute_name] # self will always have all attributes
```


Bad:
```python
# Bad
def calculate_total_price(item_list, tax_rate, discount=0):
    """
    Calculate total price.

    Args:
        item_list: List of items
        tax_rate: the tax rate to apply  
        discount: a discount, defaults to 0
    """
  ...
```


### Versioning

Given previous message sequence:
```
- database: added User table
- api: added api module with minimal code
```

Bad following messages:
```
- Modified api and ui to add user stuff
  Written by Claude

- add forgotten api method to get users
```

Good followng messages:
```
- api: implemented create_user endpoint
- api: implemented get_user endpoint
- ui: added UserView component
```


## Detecting Bad Judgment

Mistakes happen. The second best thing is to detect the symptoms and deduce their root causes, in order to prevent them or fix them.

- Function does three unrelated things? Simplicity was broken.
- Long nested conditional that's hard to parse? Readability was broken.
- Variable named `x` or `tmp` with unclear purpose? Self-evidence was broken.
- One-liner using obscure language features that confuses reviewers? Clarity was broken.
- Production error with no context about what failed or why? Observability was broken.
- Regression bug that wasn't caught because no tests exist? Testing was broken.
- Cryptic code behavior with no explanation of the "why"? Annotation was broken.
- Single massive commit mixing unrelated changes across multiple features? Versioning was broken.
