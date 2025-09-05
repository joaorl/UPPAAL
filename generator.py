# Configurations
num_dags = 3
num_procs = 3
num_actors = 3

sdf_instances = []
proc_instances = []

# =======================
# Generate SDF templates
# =======================
print("// SDF Graph template (p, d, a)")
for d in range(num_dags):
    for p in range(num_procs):
        print(f"// DAG d{d} alocado em p{p}")
        for a in range(num_actors):
            name = f"D{d}P{p}A{a}"
            print(f"{name} = sSDF({p}, {d}, {a});")
            sdf_instances.append(name)
    print()

# =======================
# Generate Processors templates
# =======================
print("// Processors templates (p, d, a)")
for d in range(num_dags):
    for p in range(num_procs):
        print(f"// DAG d{d} alocado em p{p}")
        for a in range(num_actors):
            name = f"P{p}D{d}A{a}"
            print(f"{name} = sProcessor({p}, {d}, {a});")
            proc_instances.append(name)
    print()

# =======================
# Generate System composition
# =======================
print("// =======================")
print("// System composition")
print("// =======================")
system_line = "system " + ", ".join(sdf_instances + proc_instances) + ";"
print(system_line)
