select a.apnt_no, b.pt_name, a.pt_no, a.mcdp_cd, c.dr_name, a.apnt_ymd
from appointment a, patient b, doctor c
where a.pt_no = b.pt_no
    and a.mddr_id = c.dr_id
    and to_char(a.apnt_ymd, 'YYYYMMDD') = '20220413'
    and a.mcdp_cd = 'CS'
    and apnt_cncl_yn = 'N'
order by a.apnt_ymd;