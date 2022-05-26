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