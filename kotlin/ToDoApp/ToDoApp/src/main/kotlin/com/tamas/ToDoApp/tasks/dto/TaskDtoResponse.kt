package com.tamas.ToDoApp.tasks.TaskDtoResponse

import com.tamas.ToDoApp.tasks.domain.Status
import com.tamas.ToDoApp.tasks.domain.TaskEntity

data class TaskDtoResponse(
    val id: Long,
    val name: String,
    val description: String?,
    val status: Status,
    val deadline: String?,
    val userId: Long,
    val updatedAt: String?,
    val createdAt: String?
)

fun TaskEntity.toTaskDtoResponse() = TaskDtoResponse(
    id = this.id,
    name = this.name,
    description = this.description,
    status = this.status,
    deadline = this.deadline,
    userId = this.userId,
    createdAt = this.createdAt,
    updatedAt = this.updatedAt
)

fun TaskDtoResponse.toEntity() = this.createdAt?.let {
    this.updatedAt?.let { it1 ->
        TaskEntity(
            id = this.id,
            name = this.name,
            description = this.description,
            status = this.status,
            deadline = this.deadline,
            userId = this.userId,
            createdAt = it,
            updatedAt = it1
        )
    }
}