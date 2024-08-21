import streamlit as st
import functions

todos = functions.getTodos()

def addTodo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.writeTodos(todos)

st.title("My todo app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New:",
              placeholder="Add new todo...",
              key="new_todo",
              on_change=addTodo)
