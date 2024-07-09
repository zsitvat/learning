package com.tamas.ToDoApp.tasks.controllers

import com.tamas.ToDoApp.tasks.TaskDtoRequest.TaskDtoRequest
import com.tamas.ToDoApp.tasks.TaskDtoResponse.TaskDtoResponse
import com.tamas.ToDoApp.tasks.services.TaskService
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException


@RestController
class TaskController(var taskService: TaskService) {

    @GetMapping("/tasks")
    fun getTasks(): List<TaskDtoResponse> {
        try {
            return taskService.getTasks()
        } catch (e: RuntimeException) {
            throw ResponseStatusException(HttpStatus.NOT_FOUND, "Tasks not found", e)
        }
    }

    @GetMapping("/tasks/{id}")
    fun getTaskById(@PathVariable id: Long): TaskDtoResponse? {
        try {
            return taskService.getTaskById(id)
        } catch (e: RuntimeException) {
            throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found", e)
        }
    }

    @PostMapping("/tasks/create")
    fun createTask(@RequestBody task: TaskDtoRequest): TaskDtoResponse {
        try {
            return taskService.createTask(task)
        } catch (e: RuntimeException) {
            throw ResponseStatusException(HttpStatus.BAD_REQUEST, "Task not created", e)

        }
    }

    @PostMapping("/tasks/update")
    fun updateTask(@RequestBody task: TaskDtoRequest): Boolean {
        try {
            return taskService.updateTask(task)
        } catch (e: RuntimeException) {
            throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found", e)
        }
    }

    @DeleteMapping("/tasks/delete")
    fun postTask(id: Long) {
        try {
            taskService.deleteTask(id)
        } catch (e: RuntimeException) {
            throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found", e)
        }
    }
}