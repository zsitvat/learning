package com.tamas.ToDoApp.tasks.domain

import jakarta.persistence.*
import java.time.Instant

@Entity
@Table(name = "tasks")
data class TaskEntity(
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    val id: Long = 0,

    @Column(name = "name")
    var name: String,

    @Column(name = "description")
    var description: String?,

    @Enumerated(EnumType.STRING)
    @Column(name = "status")
    var status: Status = Status.TODO,

    @Column(name = "deadline")
    var deadline: String?,

    @Column(name = "user_id")
    var userId: Long,

    @Column(name = "updated_at")
    var updatedAt: String = Instant.now().toString(),

    @Column(name = "created_at")
    var createdAt: String = Instant.now().toString()
)

enum class Status {
    TODO,
    IN_PROGRESS,
    COMPLETED
}