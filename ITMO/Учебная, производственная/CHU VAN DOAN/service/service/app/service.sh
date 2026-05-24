#!/bin/bash

USERS_DB="users/users.db"
LOGGED_IN_USER=""

function main_menu() {
  clear
  echo "======================"
  echo "      TODO List       "
  echo "======================"
  echo "1) Register"
  echo "2) Login"
  echo "3) Add a TODO Note"
  echo "4) List TODO Notes"
  echo "5) Exit"
  echo
}

function register_user() {
  echo
  echo "[+] Register [+]"

  echo -n "Enter new username: "
  read new_user

  if grep -q "^${new_user}:" "$USERS_DB" 2>/dev/null; then
    echo "[!] User '$new_user' already exists!"
    echo
    return
  fi

  echo -n "Enter new password: "
  read new_pass
  echo

  mkdir -p users 2>/dev/null
  mkdir -p notes 2>/dev/null

  echo "${new_user}:${new_pass}" >> "$USERS_DB"

  echo "[+] User '$new_user' registered successfully!"
  echo
}

function login_user() {
  echo
  echo "[+] Login [+]"

  echo -n "Username: "
  read username

  echo -n "Password: "
  read password

  echo

  if grep -q "^${username}:${password}$" "$USERS_DB" 2>/dev/null; then
    LOGGED_IN_USER="$username"
    echo "[+] Login successful! Logged in as '$LOGGED_IN_USER'."
  else
    echo "[!] Invalid credentials!"
  fi

  echo
}

function add_todo() {
  echo

  if [ -z "$LOGGED_IN_USER" ]; then
    echo "[!] You must be logged in to add notes."
    return
  fi

  echo "[+] Add a TODO note for '$LOGGED_IN_USER' [+]"

  echo -n "Enter TODO name (e.g., todo1): "
  read note_name

  note_path="notes/${LOGGED_IN_USER}---${note_name}"

  mkdir -p "notes"

  echo -n "Enter your note content: "
  read note_content

  printf '%s\n' "$note_content" > "$note_path"
  echo "[+] Note saved to '$note_path'."
  echo
}

function list_todos() {
  echo

  if [ -z "$LOGGED_IN_USER" ]; then
    echo "[!] You must be logged in to list notes."
    return
  fi

  local note_pattern="notes/${LOGGED_IN_USER}---*"

  ls $note_pattern >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "[!] No notes found for user '$LOGGED_IN_USER'."
    echo
    return
  fi

  echo "[+] TODO notes for '$LOGGED_IN_USER' [+]"
  echo "---------------------------------"

  for note_file in $note_pattern; do
    note_name="$(basename "${note_file}" | sed "s/${LOGGED_IN_USER}---//")"
    echo "TODO: ${note_name}"
    cat "$note_file"
    echo "---------------------------------"
  done

  echo
}

mkdir -p users 2>/dev/null
touch "$USERS_DB"

while true; do
  main_menu

  echo -n "Choose an option: "
  read choice

  case "$choice" in
    1)
      register_user
      ;;
    2)
      login_user
      ;;
    3)
      add_todo
      ;;
    4)
      list_todos
      ;;
    5)
      echo "[+] Exiting..."
      exit 0
      ;;
    *)
      echo
      echo "[!] Invalid selection."
      echo
      ;;
  esac

  echo "Press Enter to continue..."
  read junk
done
