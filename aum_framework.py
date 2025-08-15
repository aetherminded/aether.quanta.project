self.env_factors["inmate_engagement"] = 0.2  # 20% inmate participation
noise_factor *= (1 - self.env_factors["inmate_engagement"] * 0.15)  # Reduce noise by 3%
