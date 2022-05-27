                SELECT
                    g.*,
                    CASE WHEN AVG(r.rating) ISNULL THEN 0 ELSE AVG(r.rating) END AS Rating
                FROM raterapp_game g
                LEFT JOIN raterapp_rating r
                    ON r.game_id = g.id
                GROUP BY g.id
                ORDER BY rating DESC
                LIMIT 5


                SELECT
                    g.*,
                    CASE WHEN AVG(r.rating) ISNULL THEN 0 ELSE AVG(r.rating) END AS Rating
                FROM raterapp_game g
                LEFT JOIN raterapp_rating r
                    ON r.game_id = g.id
                GROUP BY g.id
                ORDER BY rating ASC
                LIMIT 5


                SELECT 
                    c.id,
                    c.type,
                    COUNT(gc.category_id) AS game_count
                FROM raterapp_category c
                LEFT JOIN raterapp_gamecategory gc
                    ON gc.category_id = c.id
                GROUP BY c.id


                SELECT *
                FROM raterapp_game g
                WHERE g.num_of_players > 5


                SELECT
                    *
                FROM (
                    SELECT
                        g.*,
                        COUNT(r.id) AS Reviews
                    FROM raterapp_game g
                    LEFT JOIN raterapp_review r
                        ON r.game_id = g.id
                    GROUP BY g.id
                )
                WHERE Reviews = (
                    SELECT
                        MAX(Reviews)
                    FROM (
                        SELECT
                            g.*,
                            COUNT(r.id) AS Reviews
                        FROM raterapp_game g
                        LEFT JOIN raterapp_review r
                            ON r.game_id = g.id
                        GROUP BY g.id
                    )
                )


                SELECT *
                FROM (
                        SELECT
                            gr.*,
                            u.first_name || " " || u.last_name AS full_name,
                            COUNT(g.gamer_id) AS games_added
                        FROM raterapp_gamer gr
                        LEFT JOIN raterapp_game g
                            ON gr.id = g.gamer_id
                        JOIN auth_user u
                            ON gr.id = u.id
                        GROUP BY gr.id
                )
                WHERE games_added = (
                    SELECT
                        MAX(games_added)
                    FROM (
                        SELECT
                            gr.*,
                            COUNT(g.gamer_id) AS games_added
                        FROM raterapp_gamer gr
                        LEFT JOIN raterapp_game g
                            ON gr.id = g.gamer_id
                        GROUP BY gr.id
                    )
                )