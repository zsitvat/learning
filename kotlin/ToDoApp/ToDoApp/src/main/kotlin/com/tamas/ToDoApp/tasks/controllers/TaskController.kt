package com.tamas.ToDoApp.modules.tasks.controllers

import com.tamas.ToDoApp.modules.tasks.dto.TaskDto
import com.tamas.ToDoApp.modules.tasks.services.TaskService
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RestController


@RestController
class TaskController(var taskService: TaskService) {

    @GetMapping("/tasks")
    fun getToDos():List<TaskDto> {
        return taskService.getTasks()
    }

    @GetMapping("/tasks/{id}")
    fun getTaskById(id: Long):TaskDto {
        return taskService.getTaskById(id)
    }

    @PostMapping("/tasks")
    fun postTask(task: TaskDto) {
        return taskService.postTask(task)
    }
}