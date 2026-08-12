# Library Management System (CLI)

## Business Problem
Small libraries often track book inventory and issue/return records manually, which is slow and error-prone. This project is a **command-line Library Management System** that lets a librarian add, update, delete, issue, and return books, and view which books are currently available versus issued — replacing manual record-keeping with a simple, structured program.

## About the Project
- **Type:** Python console application (single script, no external dependencies)
- **Data:** Two in-memory lists acting as the "database":
  - `books_available` — books currently in the library, each stored as `[book_id, title, author]`
  - `books_issued` — books currently checked out, same structure
- Each run starts with a pre-populated set of 10 available books and 10 issued books as sample data.

## Features (Menu Options)
1. **Add book** — add a new book after checking the ID isn't already used in either list.
2. **Update book** — edit a book's ID, name, or author by looking it up via its current ID.
3. **Delete book** — remove a book from the available list by ID.
4. **Return book** — move a book from `books_issued` back to `books_available`.
5. **Display available books** — list all books currently in the library.
6. **Display issued books** — list all books currently checked out.
7. **Issue book** — move a book from `books_available` to `books_issued`.

All list mutations (add, update, issue, return) keep `books_available`/`books_issued` sorted by book ID, and duplicate/invalid ID entries are checked before changes are applied.

## Results
- A working menu-driven CLI that performs all 7 core library operations correctly against the in-memory dataset.
- Input validation via `try/except ValueError` prevents the program from crashing on non-numeric menu input.
- A `finally: print("Thank you")` ensures a graceful exit message regardless of success or failure.

## Next Steps
- **Persist data** to a file or database (e.g. CSV, SQLite) so book records survive between runs — currently everything resets each time the script runs.
- **Loop the menu** so the user can perform multiple operations per session instead of exiting after one choice.
- **Add member/borrower tracking** (who issued which book, due dates, fines for late returns).
- **Refactor into functions** (e.g. `add_book()`, `issue_book()`) and consider a class-based design (`Book`, `Library`) for readability and easier testing.
- **Improve input validation** — e.g. reject blank titles/authors, and validate menu choices are within 1–7 without relying solely on the `else` fallback.

## Problems Faced
- **No data persistence:** since data lives only in local lists, there's no way to retain changes across separate runs of the script.
- **Single-operation sessions:** the program performs one menu action and exits, since there's no loop wrapping the menu — this makes multi-step testing (e.g. add then immediately display) require rerunning the script.
- **ID collision checks required duplicate logic:** checking whether a book ID already exists needed to loop through *both* `books_available` and `books_issued` separately in multiple places (add, update, issue), leading to repeated code blocks.
- **Nested loop variable shadowing:** reusing the loop variable `book` across nested `for` loops (e.g. in the update logic) required care to avoid overwriting the outer loop's reference mid-iteration.
- **Sorting by ID after every mutation** was necessary to keep both lists in a consistent, predictable order, but had to be manually added after each add/update/issue/return operation rather than being handled centrally.

## Tools Used
Python (standard library only — no external packages required)
