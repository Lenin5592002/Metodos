#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <unistd.h>

#define NUM_TRANSACCIONES 8   // puedes cambiarlo

typedef struct {
    int id;
    long tiempo_ns;   // tiempo por transacción en nanosegundos
} transaccion_t;

void* procesar_transaccion(void* arg) {
    transaccion_t* t = (transaccion_t*) arg;
    struct timespec inicio, fin;

    // Tiempo inicial
    clock_gettime(CLOCK_MONOTONIC, &inicio);

    // -----------------------------
    // Simulación de transacción
    // -----------------------------
    // Ejemplo: cálculo pesado
    long suma = 0;
    for (long i = 0; i < 50000000; i++) {
        suma += i;
    }

    // Tiempo final
    clock_gettime(CLOCK_MONOTONIC, &fin);

    // Calcular diferencia
    long sec = fin.tv_sec - inicio.tv_sec;
    long nsec = fin.tv_nsec - inicio.tv_nsec;

    t->tiempo_ns = sec * 1000000000L + nsec;

    pthread_exit(NULL);
}

int main() {
    pthread_t hilos[NUM_TRANSACCIONES];
    transaccion_t transacciones[NUM_TRANSACCIONES];

    struct timespec global_inicio, global_fin;

    // Tiempo inicial total
    clock_gettime(CLOCK_MONOTONIC, &global_inicio);

    // Crear hilos
    for (int i = 0; i < NUM_TRANSACCIONES; i++) {
        transacciones[i].id = i;

        if (pthread_create(&hilos[i], NULL, procesar_transaccion, &transacciones[i]) != 0) {
            perror("Error creando hilo");
            exit(1);
        }
    }

    // Esperar hilos
    for (int i = 0; i < NUM_TRANSACCIONES; i++) {
        pthread_join(hilos[i], NULL);
    }

    // Tiempo final total
    clock_gettime(CLOCK_MONOTONIC, &global_fin);

    // Cálculo tiempo total
    long sec = global_fin.tv_sec - global_inicio.tv_sec;
    long nsec = global_fin.tv_nsec - global_inicio.tv_nsec;
    long tiempo_total = sec * 1000000000L + nsec;

    // Mostrar resultados
    printf("\n=== Resultados ===\n");

    for (int i = 0; i < NUM_TRANSACCIONES; i++) {
        printf("Transacción %d: %ld ns (%.4f segundos)\n",
               transacciones[i].id,
               transacciones[i].tiempo_ns,
               transacciones[i].tiempo_ns / 1e9);
    }

    printf("\nTiempo total paralelo: %ld ns (%.4f segundos)\n",
           tiempo_total, tiempo_total / 1e9);

    return 0;
}
