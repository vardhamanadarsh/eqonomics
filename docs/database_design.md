# Eqonomics Database Design

## Users

* id (PK)
* full_name
* email
* password_hash
* role
* created_at

## Categories

* id (PK)
* name

Examples:

* CUET PG Economics
* UGC NET Economics

## TestSeries

* id (PK)
* category_id (FK)
* title
* description
* price
* total_tests
* created_at

## Tests

* id (PK)
* test_series_id (FK)
* title
* duration_minutes
* total_marks

## Questions

* id (PK)
* test_id (FK)
* question_text
* option_a
* option_b
* option_c
* option_d
* correct_answer
* explanation

## ReadingMaterials

* id (PK)
* title
* category
* file_url
* uploaded_at

## Orders

* id (PK)
* user_id (FK)
* amount
* status
* created_at

## Payments

* id (PK)
* order_id (FK)
* razorpay_payment_id
* amount
* payment_method
* status

## Attempts

* id (PK)
* user_id (FK)
* test_id (FK)
* score
* percentage
* rank
* submitted_at

## AI_News

* id (PK)
* title
* summary
* source
* category
* created_at
