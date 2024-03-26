import json
from operator import or_
from flask import Response, g, request
from . import main
from app import db
from app.models import Job
from .utils import generate_error_response
from .utils import check_manager_token

@main.route("/delete-job", methods = ["DELETE"])
@check_manager_token
def delete_job():
    if not g.user:
        return generate_error_response('UnAuthorize Access'),401
    if "job_id" not in request.args:
        return generate_error_response("job_id is not found in query parameters")
    else:
        job_id =  request.args.get('job_id')
        job = Job.query.get(job_id)
        if not job:
            return generate_error_response('job is not found'), 400
        db.session.delete(job)
        db.session.commit()
        return Response(json.dumps({'success': 'job deleted successfully',"job_id":job_id})), 200
