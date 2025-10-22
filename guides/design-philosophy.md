---
topic: Design Philosophy
trigger: Read before designing, specifying or writing code yourself. This is a fundamental guide.
version: 1.0.0
---

# Design Philosophy

Pay close attention. These are the 15 core principles of software design:

1. **Minimality**: avoid non-vital concepts, dependencies, objects, layers, state, etc.
2. **Modularity**: divide code into independent, well-defined units with clear interfaces.
3. **Layering**: separate user interface from domain logic from data storage, no leaks across boundaries.
4. **Uniqueness**: avoid conceptual and textual duplication so that things exist in only one place.
5. **Extensibility**: add seams so additions don't require rewrites.
6. **Validation**: validate early, crash loudly, give detailed errors.
7. **Consistency**: use the same patterns to solve the same problems everywhere in the codebase.
8. **Transparency**: document decisions, pending work and explicit trade-offs.
9. **Locality**: reduce scopes and side-effects, avoid globals and inject dependencies.
10. **Encapsulation**: the what is public, the how is private, the difference is clear.
11. **Focus**: work only on the task at hand, don't start adding or changing unrelated behavior.
12. **Correctness**: first make it work, then make it good, don't make it fast unless speed is necessary.
13. **Determinism**: prefer deterministic, stateless, idempotent behavior.
14. **Security**: least privilege, safe defaults, robust input handling.
15. **Flexibility**: be willing to break these rules when situations require it, but always explicitly.

These principles apply to architecture, code, documentation and planning. Users and agents are familiar with them, so you can name them when explaining, discussing or relaying instructions.


## Examples

### Minimality

Bad:
```python
class ConfigManager:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path) as f:
            return ConfigParser().parse(f.read())

class ConfigParser:
    def parse(self, text):
        return json.loads(text)
```

Good:
```python
with open(path) as f:
    config = json.load(f)
```


### Modularity

Bad:
```
interface PageController {
    setData(data: ApplicationData)
    render(root: HTMLElement)
}
```

Good:
```
interface HeaderController {
    setUser(user: User)
    setNotifications(notifications: Notification[])
    render(element: HTMLHeaderElement)
}

interface FooterController {
    setDate(date: Date)
    setConnected(isConnected: boolean)
    render(element: HTMLFooterElement)
}

interface ProductListController {
    setProducts(products: Product[])
    render(element: HTMLUListElement)
}
```


### Layering

Bad:
```
.
├── app.js
└── helpers.js
```

Good:
```
.
├── data
│   ├── api.js
│   └── db.js
├── domain
│   └── processor.js
├── ui
│   └── components.js
└── main.js
```


### Uniqueness

Bad:
```javascript

if (timeElapsed > 100) {
    console.log("Here")
} else {
    setTimeout(doFoo, 100)
}
```

Good:
```javscript
const DELAY = 100

if (timeElapsed > DELAY) {
    console.log("Here")
} else {
    setTimeout(doFoo, DELAY)
}
```


### Validation

Bad:
```python
def get_amount_text():
    return input("Enter amount") # parse later when used
```

Good:
```python
def get_amount():
    text = input("Enter amount")

    if not text:
        raise ValueError("Amount must not be empty")

    amount = int(text)

    if amount < 0:
        raise ValueError("Amount must be positive")

    elif amount > 100:
        raise ValueError("Amount must be lower than 100")

    return amount
```


### Extensibility

Bad:
```python
## Situation: parse_data is called from multiple points in the codebase.

def parse_data(path):
    with open(path) as f:
        return json.load(f)

## Problem: if we add another format or source, all those points break and must be changed.
```

Good:
```python
## Situation: parse_data is called from multiple points in the codebase.

def parse_data(stream, format):
    if format == 'json':
        return json.load(stream)
    else:
        raise ValueError(f"Format not supported: {format}")

# No problem: callers pass whatever stream (maybe file), add another format by just adding a branch.
```


### Consistency

Bad:
```javascript
function getUser(id) {
    return fetch(`/api/users/${id}`).then(r => r.json())
}

async function fetchProduct(productId) {
    const response = await fetch(`/api/products/${productId}`)
    return await response.json()
}

const loadOrder = (orderId) =>
    fetch(`/api/orders/${orderId}`).then(r => r.json())
```

Good:
```javascript
async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`)
    return await response.json()
}

async function fetchProduct(id) {
    const response = await fetch(`/api/products/${id}`)
    return await response.json()
}

async function fetchOrder(id) {
    const response = await fetch(`/api/orders/${id}`)
    return await response.json()
}
```


### Transparency

Bad:
```python
def process(data):
    # Clean and transform data
    result = data.strip().lower()
    return result if len(result) > 3 else None  # Why 3?
```

Good:
```python
MIN_VALID_LENGTH = 3  # Reject abbreviations, require full names

def process(data):
    """Normalize data by stripping whitespace and converting to lowercase.

    Returns None for inputs shorter than MIN_VALID_LENGTH to filter out
    abbreviations while accepting full names.
    """
    result = data.strip().lower()
    return result if len(result) >= MIN_VALID_LENGTH else None
```


### Locality

Bad:
```javascript
import { options } from './options'
import { processPayment } from './helpers'

let total = 0

function addToCart(item) {
    total += item.price * options.multiplier
    items.push(item)
}

function checkout() {
    processPayment(total)
    total = 0
}
```

Good:
```javascript
function addToCart(cart, item, options) {
    return {
        items: [...cart.items, item],
        total: cart.total + item.price * options.multiplier
    }
}

function checkout(cart, paymentProcessor) {
    paymentProcessor.process(cart)
    return { items: [], total: 0 }
}
```


### Encapsulation

Bad:
```python
class User:
    def __init__(self, name):
        self.name = name
        self.password_hash = None

user = User("Alice")
user.password_hash = hashlib.sha256(password.encode()).hexdigest()
```

Good:
```python
class User:
    def __init__(self, name):
        self.name = name
        self._password_hash = None

    def set_password(self, password):
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

user = User("Alice")
user.set_password(password)
```


### Focus

Bad:
```python
## Task: implement method to save users.

def save_user(user):
    db.insert('users', user)

## Implement verification emails while we're at it.
def send_email(user):
    new_email_module.send_email(user)
```

Good:
```python
## Task: implement method to save users.

def save_user(user):
    """Save user to database."""
    db.insert('users', user)

## Task completed. Nothing else added.
```


### Correctness

Bad:
```javascript
function calculateAverage(numbers) {
    // Make it fast with reduce!
    return numbers.reduce((sum, n) => sum + n, 0) / numbers.length
}

calculateAverage([])  // NaN - broken but "fast"
```

Good:
```javascript
function calculateAverage(numbers) {
    if (numbers.length === 0) {
        throw new Error("Cannot calculate average of empty array")
    }

    const sum = numbers.reduce((acc, n) => acc + n, 0)
    return sum / numbers.length
}

// Only optimize if profiling shows this is a bottleneck
```


### Determinism

Bad:
```python
def get_greeting(user):
    greetings = ["Hello", "Hi", "Hey"]
    return f"{random.choice(greetings)}, {user.name}!"
```

Good:
```python
def get_greeting(user):
    return f"Hello, {user.name}!"

## If variation is truly needed:
def get_greeting(user, seed=None):
    greetings = ["Hello", "Hi", "Hey"]
    rng = random.Random(seed) if seed else random.Random(user.id)
    return f"{rng.choice(greetings)}, {user.name}!"
```


### Security

Bad:
```python
def run_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return db.execute(query)
```

Good:
```python
def run_query(user_input):
    # Parameterized queries prevent SQL injection
    query = "SELECT * FROM users WHERE name = ?"
    return db.execute(query, [user_input])
```


### Flexibility

Flexibility in application of these principles is about finding balance and avoiding absolutes. Here are some guidelines, examples and common pitfalls.

#### Resolving Conflicts

Scenario: minimality conflicts with extensibility.

- Just starting a feature? Minimality usually wins.
- Second time changing this code for similar reasons? Extensibility usually wins.
- Adding parameters you don't use "just in case"? Minimality usually wins.


#### Striking a Balance

Scenario: considering adding a cache to a data layer.

- Minimality says: don't add complexity yet
- Correctness says: we need it because this is a very clear bottleneck and will fail at its job otherwise
- Extensibility says: make caching strategies pluggable

Balance: add a rudimentary in-memory cache (minimality), wrap behind interface for future replacement (extensibility), see in practice whether this performance gain is enough to satisfy and is once again secondary (correctness). Document conflict and resolution (transparency).


#### Detecting Bad Judgment

Mistakes happen. The second best thing is to detect the symptoms and deduce their root causes, in order to prevent them or fix them.

- Five cases when only one is actually used? Minimality was broken.
- Same class providing two distinct functionalities breaks becase one changed? Modularity was broken.
- Type problems reading from the database in the UI? Layering was broken.
- Changed a number in one place, forgot to change it in another? Uniqueness was broken.
- Changing 10 files because of a minor adjustment? Extensibility was broken.
- Cryptic error from bad value far away from where the value originated? Validation was broken.
- Naming differences for the same quality causing confusion? Consistency was broken.
- Strange past tradeoff with no explanation? Transparency was broken.
- Problems because a setting must be treated differently but was taken from a global object? Locality was broken.
- Injecting supposedly internal state into an object? Encapsulation was broken.
- Difficulty deciding on a commit message because two independent things were done? Focus was broken.
- Super fast but complex algorithm for a rare task with small inputs? Correctness was broken.
- Can't reproduce an error because of randomness or untraceable side-effects? Determinism was broken.
- Bad data in an SQL table because input was saved verbatim? Security was broken.


#### Knowingly Breaking Principles

Principles can be deliberately violated when:

- External requirements force it (client demands, compliance, legacy compatibility)
- Prototyping or experimentation (temporary priority of speed over quality)
- Technical constraints leave no alternative (platform limitations, dependency requirements)


## Humility and Trust

Finally, understand that even the best software engineers need colleagues. When in doubt, rely on the user to provide guidance and feedback.
