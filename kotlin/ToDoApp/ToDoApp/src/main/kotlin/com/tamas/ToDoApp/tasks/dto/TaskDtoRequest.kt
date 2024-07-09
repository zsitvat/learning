package com.tamas.ToDoApp.tasks.TaskDtoRequest

import com.tamas.ToDoApp.tasks.domain.Status
import com.tamas.ToDoApp.tasks.domain.TaskEntity
import java.time.Instant

data class TaskDtoRequest(
    val id: Long,
    val name: String,
    val description: String?,
    val status: Status,
    val deadline: String?,
    val userId: Long,
    val updatedAt: String?,
    val createdAt: String?
)

fun TaskEntity.toTaskDtoRequest() = TaskDtoRequest(
    id = this.id,
    name = this.name,
    description = this.description,
    status = this.status,
    deadline = this.deadline,
    userId = this.userId,
    createdAt = this.createdAt,
    updatedAt = this.updatedAt
)

fun TaskDtoRequest.toEntity() = TaskEntity(
    id = this.id,
    name = this.name,
    description = this.description,
    status = this.status,
    deadline = this.deadline,
    userId = this.userId,
    createdAt = this.createdAt ?: Instant.now().toString(),
    updatedAt = this.updatedAt ?: Instant.now().toString()
)