SUMMARY_PROMPT = """
Summarize this loan application in 3-4 sentences.
Be factual and neutral.
Do not add or assume information that is not stated.
Do not say whether the loan should be approved or rejected.
"""

EXTRACT_PROMPT = """
Extract the following fields from the loan application:

applicant_name
amount_ghs
purpose
monthly_profit_ghs
has_collateral_or_guarantor
repayment_months

Return only valid JSON.

If a field is not stated, use null.
Do not guess.
"""

BRIEF_PROMPT = """
Review the loan application and extracted information.

Give the response using these four sections:

1. Strengths
2. Risks / red flags
3. Missing information
4. Suggested next step

Use only information stated in the letter or extracted data.
Do not invent or assume information.
Do not approve or reject the loan.
The final decision must be made by a human.
"""