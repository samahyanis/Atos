from datetime import timedelta

from django.db import models

# Create your models here.
class Nuit_applicatif(models.Model):
    type_na                = models.CharField(max_length=120, null=True)
    Environnement_na       = models.CharField(max_length=120, null=True)
    Date_na                = models.DateField()
    Durée_na               = models.DecimalField(decimal_places=2, max_digits=1000000)
    moyenne_execution_na   = models.DecimalField(decimal_places=2, max_digits=1000000)


class Detail_na(models.Model):
    nuit_applicatif        = models.ForeignKey(Nuit_applicatif, on_delete=models.CASCADE, null=True)
    Nom_job                = models.CharField(max_length=120, null=True)
    Date_heure_debut_na    = models.DateTimeField()
    Date_heure_fin_na      = models.DateTimeField()
    Statut_job             = models.CharField(max_length=120, null=True)


class Detail_job(models.Model):
    detail_job             = models.ForeignKey(Detail_na, on_delete=models.CASCADE, null=True)
    moyenne_execution_job  = models.DecimalField(decimal_places=2, max_digits=1000000)


class History(models.Model):
    job_id            = models.CharField(("job_id"), max_length=255,  null=True)
    order_id            = models.CharField(("order_id"), max_length=255,  null=True)
    workloads            = models.CharField(("workloads"), max_length=255,  null=True)
    data_center               = models.CharField(("data_center"), max_length=255,  null=True )
    sched_table             = models.CharField(("sched_table"), max_length=255,  null=True)
    dsn             = models.CharField(("dsn"), max_length=255, null=True)
    job_mem_name             = models.CharField(("job_mem_name"), max_length=255, null=True)
    application               = models.CharField(("application"), max_length=255, null=True)
    group_name             = models.CharField(("group_name"), max_length=255, null=True)
    owner             = models.CharField(("owner"), max_length=255, null=True)
    node_group             = models.CharField(("node_group"), max_length=255, null=True)
    node_id             = models.CharField(("node_id"), max_length=255, null=True)
    start_time             = models.CharField(("start_time"), max_length=255, null=True)
    end_time             = models.CharField(("end_time"), max_length=255, null=True)
    order_date             = models.CharField(("order_date"), max_length=255, null=True)
    rerun_counter             = models.CharField(("rerun_counter"), max_length=255, null=True)
    ended_status             = models.CharField(("ended_status"), max_length=255, null=True)
    run_time_sec             = models.CharField(("run_time_sec"), max_length=255, null=True)
    start_time_idx             = models.CharField(("start_time_idx"), max_length=255, null=True)
    end_time_idx             = models.CharField(("end_time_idx"), max_length=255, null=True)
    start_date_idx             = models.CharField(("start_date_idx"), max_length=255, null=True)
    end_date_idx             = models.CharField(("end_date_idx"), max_length=255, null=True)
    stat_cal_ctm             = models.CharField(("stat_cal_ctm"), max_length=255, null=True)
    stat_cal             = models.CharField(("stat_cal"), max_length=255, null=True)
    stat_period             = models.CharField(("stat_period"), max_length=255, null=True)
    cpu_time             = models.CharField(("cpu_time"), max_length=255, null=True)
    status             = models.CharField(("status"), max_length=255, null=True)
    agent_elapsed_time             = models.CharField(("agent_elapsed_time"), max_length=255, null=True)

    from datetime import timedelta

    # @property
    # def exec_time(self):
    #     end = timedelta(int(self.end_time.hour, self.endtime.minute, self.endtime.second)
    #     start = timedelta(self.starttime.hour, self.starttime.minute, self.starttime.second)
    #     return end - start


    class Meta:
        db_table = 'yanis_origin'
