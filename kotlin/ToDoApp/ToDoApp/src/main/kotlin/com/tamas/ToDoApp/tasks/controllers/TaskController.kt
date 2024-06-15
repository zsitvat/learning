package com.tamas.ToDoApp.tasks.controllers

import com.tamas.ToDoApp.tasks.services.TaskService
import com.tamas.ToDoApp.tasks.dto.TaskDto
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RestController


@RestController
class TaskController(val taskService: TaskService) {

    @GetMapping("/tasks")
    fun getToDos():List<TaskDto> {
        return taskService.getTasks()
    }

    @GetMapping("/tasks/{id}")
    fun getTaskById(id: Long): TaskDto {
        return taskService.getTaskById(id)
    }

    @PostMapping("/tasks/create")
    fun postTask(task: TaskDto) {
        return taskService.postTask(task)
    }
}