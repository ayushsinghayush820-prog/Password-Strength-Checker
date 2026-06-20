# Password-Strength-Checker

A Python tool that evaluates password strength against 
five enterprise security criteria and returns a 
Weak / Medium / Strong rating.

## Security Context

Password policy enforcement is a mandatory control in every 
enterprise security framework:
**web app auth modules**  enforce these rules programmatically — this tool demonstrates that logic

## What it checks 
- **length** - Minimum 8 characters
- **Uppercase** - At least one upper letter
- **Lowecase** - At least one Lower letter
- **Digits**- At least one digit there 
- **Special Characters**- At least one `!@#$%^&*` etc

  **Rating logic:** 5/5 criteria = Strong · 3–4/5 = Medium · <3 = Weak


## How to run
  1. Install Phython
  2. Run; python password checker.py
  3. Enter your password after prompt run

## Technical implementation

- `len()` for length validation
- `any()` with generator expressions for character class checks
- `string` module constants: `string.ascii_uppercase`, 
  `string.digits`, `string.punctuation`


## What I learned

- How authentication systems enforce password policy at code level
- Why each criterion matters (uppercase+special = defeats 
  dictionary attacks, length = defeats brute force)
- Connection between password policy and real frameworks 
 
