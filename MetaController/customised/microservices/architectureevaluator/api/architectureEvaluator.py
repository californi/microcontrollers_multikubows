class ArchitectureDesiredNoCpuFailureRate:
    maxCpuFailureRate = "0.0"
    scalabilityaDesiredReplicas = "1"
    fidelityaDesiredReplicas = "1"
    scalabilitybDesiredReplicas = "0"
    fidelitybDesiredReplicas = "0"


class ArchitectureDesiredLowCpuFailureRate:
    maxCpuFailureRate = "0.5"
    scalabilityaDesiredReplicas = "0"
    fidelityaDesiredReplicas = "1"
    scalabilitybDesiredReplicas = "1"
    fidelitybDesiredReplicas = "0"


class ArchitectureDesiredHighCpuFailureRate:
    maxCpuFailureRate = "1.0"
    scalabilityaDesiredReplicas = "0"
    fidelityaDesiredReplicas = "0"
    scalabilitybDesiredReplicas = "1"
    fidelitybDesiredReplicas = "1"

# this function needs to be refactored
# json from database


def isArchitectureOK(currentArchitecture):
    cpuFailureRate = float(currentArchitecture[0]["property_value"])
    # currentArchitecture[0][2]  # FailureManager
    # currentArchitecture[0][3]  # cpuFailureRate
    # currentArchitecture[0][4]  # value of cpuFailureRate
    if(cpuFailureRate == 0.0):
        # currentArchitecture[1][2]  # Scalabilitya
        # currentArchitecture[1][3]  # desiredReplicas
        # currentArchitecture[1][4]  # value of desiredReplicas
        booScalabilitya = currentArchitecture[1][
            "property_value"] == ArchitectureDesiredNoCpuFailureRate.scalabilityaDesiredReplicas

        # currentArchitecture[2][2]  # Fidelitya
        # currentArchitecture[2][3]  # desiredReplicas
        # currentArchitecture[2][4]  # value of desiredReplicas
        booFidelitya = currentArchitecture[2]["property_value"] == ArchitectureDesiredNoCpuFailureRate.fidelityaDesiredReplicas

        # currentArchitecture[3][2]  # Scalabilityb
        # currentArchitecture[3][3]  # desiredReplicas
        # currentArchitecture[3][4]  # value of desiredReplicas
        booScalabilityb = currentArchitecture[3][
            "property_value"] == ArchitectureDesiredNoCpuFailureRate.scalabilitybDesiredReplicas

        # currentArchitecture[4][2]  # Fidelityb
        # currentArchitecture[4][3]  # desiredReplicas
        # currentArchitecture[4][4]  # value of desiredReplicas
        booFidelityb = currentArchitecture[4]["property_value"] == ArchitectureDesiredNoCpuFailureRate.fidelitybDesiredReplicas

        return (booScalabilitya and booFidelitya and booScalabilityb and booFidelityb)

    elif (cpuFailureRate > 0.0 and cpuFailureRate <= 0.5):
        # currentArchitecture[1][2]  # Scalabilitya
        # currentArchitecture[1][3]  # desiredReplicas
        # currentArchitecture[1][4]  # value of desiredReplicas
        booScalabilitya = currentArchitecture[1]["property_value"] == ArchitectureDesiredLowCpuFailureRate.scalabilityaDesiredReplicas

        # currentArchitecture[2][2]  # Fidelitya
        # currentArchitecture[2][3]  # desiredReplicas
        # currentArchitecture[2][4]  # value of desiredReplicas
        booFidelitya = currentArchitecture[2]["property_value"] == ArchitectureDesiredLowCpuFailureRate.fidelityaDesiredReplicas

        # currentArchitecture[3][2]  # Scalabilityb
        # currentArchitecture[3][3]  # desiredReplicas
        # currentArchitecture[3][4]  # value of desiredReplicas
        booScalabilityb = currentArchitecture[3]["property_value"] == ArchitectureDesiredLowCpuFailureRate.scalabilitybDesiredReplicas

        # currentArchitecture[4][2]  # Fidelityb
        # currentArchitecture[4][3]  # desiredReplicas
        # currentArchitecture[4][4]  # value of desiredReplicas
        booFidelityb = currentArchitecture[4]["property_value"] == ArchitectureDesiredLowCpuFailureRate.fidelitybDesiredReplicas

        return (booScalabilitya and booFidelitya and booScalabilityb and booFidelityb)
    else:
        # currentArchitecture[1][2]  # Scalabilitya
        # currentArchitecture[1][3]  # desiredReplicas
        # currentArchitecture[1][4]  # value of desiredReplicas
        booScalabilitya = currentArchitecture[1]["property_value"] == ArchitectureDesiredHighCpuFailureRate.scalabilityaDesiredReplicas

        # currentArchitecture[2][2]  # Fidelitya
        # currentArchitecture[2][3]  # desiredReplicas
        # currentArchitecture[2][4]  # value of desiredReplicas
        booFidelitya = currentArchitecture[2]["property_value"] == ArchitectureDesiredHighCpuFailureRate.fidelityaDesiredReplicas

        # currentArchitecture[3][2]  # Scalabilityb
        # currentArchitecture[3][3]  # desiredReplicas
        # currentArchitecture[3][4]  # value of desiredReplicas
        booScalabilityb = currentArchitecture[3]["property_value"] == ArchitectureDesiredHighCpuFailureRate.scalabilitybDesiredReplicas

        # currentArchitecture[4][2]  # Fidelityb
        # currentArchitecture[4][3]  # desiredReplicas
        # currentArchitecture[4][4]  # value of desiredReplicas
        booFidelityb = currentArchitecture[4]["property_value"] == ArchitectureDesiredHighCpuFailureRate.fidelitybDesiredReplicas

        return (booScalabilitya and booFidelitya and booScalabilityb and booFidelityb)
