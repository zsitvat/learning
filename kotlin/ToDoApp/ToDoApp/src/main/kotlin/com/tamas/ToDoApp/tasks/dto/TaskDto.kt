package com.tamas.ToDoApp.modules.tasks.dto

import com.tamas.ToDoApp.modules.tasks.repository.TaskEntity

data class TaskDto(
    val id: Long,
    val name: String,
    val description: String,
    val status: Status,
    val deadline: Int,
    val userId: Long,
    val updatedAt: Int,
    val createdAt: Int
) {

    enum class Status {
        PENDING,
        COMPLETED
    }

    fun toEntity() = TaskEntity(
        id = this.id,
        name = this.name,
        description = this.description,
        status = this.status,
        deadline = this.deadline,
        userId = this.userId,
        updatedAt = this.updatedAt,
        createdAt = this.createdAt
    )
}
